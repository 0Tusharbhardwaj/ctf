#!/usr/bin/env python3
import struct

PCVM_MAGIC = 0x4D564350  # "PCVM"
PCVM_VERSION = 1

# Opcodes
OP_NOP        = 0x00
OP_LOAD_IMM   = 0x01
OP_MOV        = 0x02
OP_ADD        = 0x03
OP_SUB        = 0x04
OP_SHL        = 0x05
OP_OR         = 0x06
OP_ALLOC_RAW  = 0x10
OP_ALLOC_BOX  = 0x11
OP_PIN        = 0x12
OP_UNPIN      = 0x13
OP_DERIVE_PTR = 0x14
OP_LOAD_WORD  = 0x15
OP_STORE_WORD = 0x16
OP_GC         = 0x20
OP_EMIT_HASH  = 0x30
OP_HALT       = 0xFF

# Proof Rule Types
PROOF_RULE_PINNED_STABILITY = 0x01

class Instruction:
    def __init__(self, opcode, r_dst=0, r_src1=0, r_src2=0, imm=0):
        self.opcode = opcode
        self.r_dst = r_dst
        self.r_src1 = r_src1
        self.r_src2 = r_src2
        self.imm = imm

    def pack(self):
        return struct.pack("<BBBB i", self.opcode, self.r_dst, self.r_src1, self.r_src2, self.imm)

class ProofRule:
    def __init__(self, rule_type, reg_interior, reg_parent, pc_valid_from, pc_valid_to):
        self.rule_type = rule_type
        self.reg_interior = reg_interior
        self.reg_parent = reg_parent
        self.pc_valid_from = pc_valid_from
        self.pc_valid_to = pc_valid_to

    def pack(self):
        return struct.pack("<HBB II", self.rule_type, self.reg_interior, self.reg_parent,
                           self.pc_valid_from, self.pc_valid_to)

class ProgramBuilder:
    def __init__(self):
        self.instructions = []
        self.proof_rules = []

    def current_pc(self):
        return len(self.instructions)

    def nop(self):
        self.instructions.append(Instruction(OP_NOP))
        return self

    def load_imm(self, r_dst, imm):
        self.instructions.append(Instruction(OP_LOAD_IMM, r_dst=r_dst, imm=imm))
        return self

    def mov(self, r_dst, r_src1):
        self.instructions.append(Instruction(OP_MOV, r_dst=r_dst, r_src1=r_src1))
        return self

    def add(self, r_dst, r_src1, r_src2):
        self.instructions.append(Instruction(OP_ADD, r_dst=r_dst, r_src1=r_src1, r_src2=r_src2))
        return self

    def sub(self, r_dst, r_src1, r_src2):
        self.instructions.append(Instruction(OP_SUB, r_dst=r_dst, r_src1=r_src1, r_src2=r_src2))
        return self

    def shl(self, r_dst, r_src1, imm):
        self.instructions.append(Instruction(OP_SHL, r_dst=r_dst, r_src1=r_src1, imm=imm))
        return self

    def or_op(self, r_dst, r_src1, r_src2):
        self.instructions.append(Instruction(OP_OR, r_dst=r_dst, r_src1=r_src1, r_src2=r_src2))
        return self

    def alloc_raw(self, r_dst, words):
        self.instructions.append(Instruction(OP_ALLOC_RAW, r_dst=r_dst, imm=words))
        return self

    def alloc_box(self, r_dst, r_child):
        self.instructions.append(Instruction(OP_ALLOC_BOX, r_dst=r_dst, r_src1=r_child))
        return self

    def pin(self, r_obj):
        self.instructions.append(Instruction(OP_PIN, r_src1=r_obj))
        return self

    def unpin(self, r_obj):
        self.instructions.append(Instruction(OP_UNPIN, r_src1=r_obj))
        return self

    def derive_ptr(self, r_dst, r_obj, offset):
        self.instructions.append(Instruction(OP_DERIVE_PTR, r_dst=r_dst, r_src1=r_obj, imm=offset))
        return self

    def load_word(self, r_dst, r_src, offset):
        self.instructions.append(Instruction(OP_LOAD_WORD, r_dst=r_dst, r_src1=r_src, imm=offset))
        return self

    def store_word(self, r_target, offset, r_val):
        self.instructions.append(Instruction(OP_STORE_WORD, r_src1=r_target, r_src2=r_val, imm=offset))
        return self

    def gc(self):
        self.instructions.append(Instruction(OP_GC))
        return self

    def emit_hash(self, r_src):
        self.instructions.append(Instruction(OP_EMIT_HASH, r_src1=r_src))
        return self

    def halt(self):
        self.instructions.append(Instruction(OP_HALT))
        return self

    def add_proof_rule(self, rule_type, reg_interior, reg_parent, pc_valid_from, pc_valid_to):
        self.proof_rules.append(ProofRule(rule_type, reg_interior, reg_parent, pc_valid_from, pc_valid_to))
        return self

    def build(self):
        header = struct.pack("<IHHII",
                             PCVM_MAGIC,
                             PCVM_VERSION,
                             len(self.proof_rules),
                             len(self.instructions),
                             0)
        proof_bytes = b"".join(r.pack() for r in self.proof_rules)
        insn_bytes = b"".join(i.pack() for i in self.instructions)
        return header + proof_bytes + insn_bytes
