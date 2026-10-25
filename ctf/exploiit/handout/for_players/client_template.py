#!/usr/bin/env python3
"""
SafeScript PCVM Client Template
Use this script to assemble and send bytecode + capability proofs to the challenge.
"""
import sys
import socket
import base64
from gen_proof import ProgramBuilder, PROOF_RULE_PINNED_STABILITY

HOST = "localhost"
PORT = 1337

def build_program():
    builder = ProgramBuilder()
    
    # -------------------------------------------------------------
    # Write your bytecode instructions and capability proofs here!
    # Available builder methods:
    #   builder.alloc_raw(r_dst, words)
    #   builder.alloc_box(r_dst, r_child)
    #   builder.pin(r_obj)
    #   builder.unpin(r_obj)
    #   builder.derive_ptr(r_dst, r_obj, offset)
    #   builder.load_word(r_dst, r_src, offset)
    #   builder.store_word(r_target, offset, r_val)
    #   builder.load_imm(r_dst, imm)
    #   builder.shl(r_dst, r_src, imm)
    #   builder.or_op(r_dst, r_src1, r_src2)
    #   builder.gc()
    #   builder.emit_hash(r_src)
    #   builder.halt()
    #   builder.add_proof_rule(rule_type, reg_interior, reg_parent, pc_valid_from, pc_valid_to)
    # -------------------------------------------------------------

    # Example: Allocate buffer, store value, halt
    builder.alloc_raw(r_dst=0, words=5)
    builder.load_imm(r_dst=1, imm=1337)
    builder.store_word(r_target=0, offset=0, r_val=1)
    builder.halt()

    return builder.build()

def main():
    payload = build_program()
    b64_payload = base64.b64encode(payload) + b"\n"

    print(f"[*] Connecting to {HOST}:{PORT}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Read banner
    banner = s.recv(1024).decode(errors="replace")
    print(banner, end="")

    # Send payload
    s.sendall(b64_payload)

    # Read response
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(data.decode(errors="replace"), end="")
    s.close()

if __name__ == "__main__":
    main()
