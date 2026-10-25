#ifndef PCVM_COMMON_H
#define PCVM_COMMON_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#define PCVM_MAGIC 0x4D564350  /* "PCVM" in little-endian */
#define PCVM_VERSION 1

#define PCVM_NUM_REGS 16
#define PCVM_HEAP_SIZE (64 * 1024)   /* 64 KB nursery heap */
#define PCVM_MAX_INSTRUCTIONS 2048
#define PCVM_MAX_PROOF_RULES 256
#define PCVM_SECRET_SIZE 32          /* 32-byte instance secret */

/* Opcodes */
typedef enum {
    OP_NOP          = 0x00,
    OP_LOAD_IMM     = 0x01,  /* r_dst = imm */
    OP_MOV          = 0x02,  /* r_dst = r_src1 */
    OP_ADD          = 0x03,  /* r_dst = r_src1 + r_src2 */
    OP_SUB          = 0x04,  /* r_dst = r_src1 - r_src2 */
    OP_SHL          = 0x05,  /* r_dst = r_src1 << imm */
    OP_OR           = 0x06,  /* r_dst = r_src1 | r_src2 */
    OP_ALLOC_RAW    = 0x10,  /* r_dst = alloc_raw(words = imm) */
    OP_ALLOC_BOX    = 0x11,  /* r_dst = alloc_box(child = r_src1) */
    OP_PIN          = 0x12,  /* pin(r_src1) */
    OP_UNPIN        = 0x13,  /* unpin(r_src1) */
    OP_DERIVE_PTR   = 0x14,  /* r_dst = derive_interior(r_src1, offset = imm) */
    OP_LOAD_WORD    = 0x15,  /* r_dst = read_word(ptr = r_src1, offset = imm) */
    OP_STORE_WORD   = 0x16,  /* write_word(ptr = r_src1, offset = imm, val = r_src2) */
    OP_GC           = 0x20,  /* trigger compacting GC */
    OP_EMIT_HASH    = 0x30,  /* feed r_src1 (uint64) into instance HMAC */
    OP_HALT         = 0xFF   /* terminate execution */
} pcvm_opcode_t;

/* Binary Instruction Representation (8 bytes each) */
typedef struct {
    uint8_t opcode;
    uint8_t r_dst;
    uint8_t r_src1;
    uint8_t r_src2;
    int32_t imm;
} __attribute__((packed)) pcvm_insn_t;

/* Proof Certificate Types */
typedef enum {
    PROOF_RULE_NONE             = 0x00,
    PROOF_RULE_PINNED_STABILITY = 0x01  /* Asserts interior ptr is immune across GC */
} pcvm_proof_type_t;

/* Proof Certificate Representation (12 bytes each) */
typedef struct {
    uint16_t rule_type;      /* pcvm_proof_type_t */
    uint8_t  reg_interior;   /* Register holding the interior pointer */
    uint8_t  reg_parent;     /* Register holding the parent object */
    uint32_t pc_valid_from;  /* Instruction offset where certificate starts */
    uint32_t pc_valid_to;    /* Instruction offset where certificate ends */
} __attribute__((packed)) pcvm_proof_rule_t;

/* Binary File Header (16 bytes) */
typedef struct {
    uint32_t magic;           /* PCVM_MAGIC */
    uint16_t version;         /* PCVM_VERSION */
    uint16_t num_proof_rules; /* count of pcvm_proof_rule_t entries */
    uint32_t code_size;       /* count of pcvm_insn_t entries */
    uint32_t reserved;        /* must be 0 */
} __attribute__((packed)) pcvm_header_t;

/* Heap Object Types */
typedef enum {
    OBJ_FREE       = 0,
    OBJ_RAW_BUFFER = 1,
    OBJ_BOX        = 2
} pcvm_obj_type_t;

#define OBJ_FLAG_PINNED 0x0001
#define OBJ_FLAG_MARKED 0x0002

/* Object Header stored on the heap preceding payload */
typedef struct {
    uint16_t type;         /* pcvm_obj_type_t */
    uint16_t flags;        /* OBJ_FLAG_* */
    uint32_t size_words;   /* Payload size in 64-bit words */
    uint64_t forward_addr; /* Relocation address during compaction */
} __attribute__((aligned(8))) pcvm_obj_header_t;

#endif /* PCVM_COMMON_H */
