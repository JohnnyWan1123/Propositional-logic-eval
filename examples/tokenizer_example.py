from evaluation_function.parsing import Tokenizer, TokenType


def tokenize_string(text: str):
    print(f"Input: {text}")
    print("-" * 60)
    
    tokenizer = Tokenizer(text)
    tokens = []
    
    try:
        while True:
            token = tokenizer.next_token()
            tokens.append(token)
            
            if token.type == TokenType.EOF:
                break
            
            print(f"  {token}")
    except ValueError as e:
        print(f"  ERROR: {e}")
        return None
    
    print(f"\nTotal tokens: {len(tokens) - 1} (excluding EOF)")
    print()
    return tokens


def main():
    print("=" * 60)
    print("Tokenizer Examples for Propositional Logic")
    print("=" * 60)
    print()
    
    test_strings = [
        "p",
        "p'",
        "p''",
        "q",
        "r",
        "⊤",
        "⊥",
        "¬p",
        "p ∧ q",
        "p ∨ q",
        "p → q",
        "p ↔ q",
        "p ∧ q ∨ r",
        "p → q → r",
        "¬p ∧ q",
        "p ∧ (q ∨ r)",
        "(p → q) → r",
        "p ↔ (q ↔ r)",
        "¬(p ∧ q)",
        "((p → q) ∧ (q → r)) → (p → r)",
        "¬(p ∨ q) ↔ (¬p ∧ ¬q)",
        "p ∧ q ∧ r",
        "p ∨ q ∨ r",
        "p ∧ q → r ∨ s",
    ]
    
    for test_string in test_strings:
        tokenize_string(test_string)
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
