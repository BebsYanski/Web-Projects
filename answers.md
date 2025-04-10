
# Logic, Truth Tables, Logic Gates, and Number Systems Exam - Answer Key

## Section 1: Number Systems (20 points)

1. **(4 points)** Convert the following decimal numbers to binary:
    * (a) 25 = 11001
    * (b) 42 = 101010

2. **(4 points)** Convert the following binary numbers to decimal:
    * (a) 11010 = 26
    * (b) 101111 = 47

3. **(4 points)** Convert the following hexadecimal numbers to decimal:
    * (a) 2A = 42
    * (b) 1F = 31

4. **(4 points)** Convert the following decimal numbers to hexadecimal:
    * (a) 35 = 23
    * (b) 60 = 3C

5. **(4 points)** Perform the following binary addition: 1011 + 1101 = 11000

## Section 2: Logic Gates (20 points)

1. **(5 points)** Draw the symbol for each of the following logic gates:
    * (a) AND gate: (Standard AND gate symbol)
    * (b) OR gate: (Standard OR gate symbol)
    * (c) NOT gate: (Standard NOT gate symbol)
    * (d) XOR gate: (Standard XOR gate symbol)
    * (e) NAND gate: (Standard NAND gate symbol)

2. **(5 points)** Write the truth table for an OR gate with two inputs (A and B).

    | A | B | Output |
    |---|---|--------|
    | 0 | 0 | 0      |
    | 0 | 1 | 1      |
    | 1 | 0 | 1      |
    | 1 | 1 | 1      |

3. **(5 points)** Write the truth table for a NOT gate.

    | A | Output |
    |---|--------|
    | 0 | 1      |
    | 1 | 0      |

4. **(5 points)** Draw a logic circuit that represents the Boolean expression: $A \cdot (B + \overline{C})$
    * (Draw an OR gate with inputs B and NOT C, then an AND gate with input A and the output from the OR gate)

## Section 3: Truth Tables (30 points)

1. **(10 points)** Construct the truth table for the following Boolean expression: $(A \cdot B) + \overline{C}$

    | A | B | C | A.B | NOT C | (A.B) + NOT C |
    |---|---|---|-----|-------|---------------|
    | 0 | 0 | 0 | 0   | 1     | 1             |
    | 0 | 0 | 1 | 0   | 0     | 0             |
    | 0 | 1 | 0 | 0   | 1     | 1             |
    | 0 | 1 | 1 | 0   | 0     | 0             |
    | 1 | 0 | 0 | 0   | 1     | 1             |
    | 1 | 0 | 1 | 0   | 0     | 0             |
    | 1 | 1 | 0 | 1   | 1     | 1             |
    | 1 | 1 | 1 | 1   | 0     | 1             |

2. **(10 points)** Construct the truth table for the following Boolean expression: $A \oplus (B \cdot \overline{A})$

    | A | B | NOT A | B.NOT A | A XOR (B.NOT A) |
    |---|---|-------|---------|-----------------|
    | 0 | 0 | 1     | 0       | 0               |
    | 0 | 1 | 1     | 1       | 1               |
    | 1 | 0 | 0     | 0       | 1               |
    | 1 | 1 | 0     | 0       | 1               |

3. **(10 points)** Given the following truth table, write the Boolean expression:

    | A | B | C | Output |
    |---|---|---|--------|
    | 0 | 0 | 0 | 0      |
    | 0 | 0 | 1 | 1      |
    | 0 | 1 | 0 | 0      |
    | 0 | 1 | 1 | 1      |
    | 1 | 0 | 0 | 0      |
    | 1 | 0 | 1 | 0      |
    | 1 | 1 | 0 | 1      |
    | 1 | 1 | 1 | 1      |

    * Expression: $(\overline{A} \cdot \overline{B} \cdot C) + (\overline{A} \cdot B \cdot C) + (A \cdot B \cdot \overline{C}) + (A \cdot B \cdot C)$
    * Simplified expression: $\overline{A} \cdot C + A \cdot B$

## Section 4: Boolean Algebra (30 points)

1. **(10 points)** Simplify the following Boolean expression using Boolean algebra laws: $A \cdot (A + B)$
    * $A \cdot A + A \cdot B = A + A \cdot B = A \cdot (1 + B) = A \cdot 1 = A$

2. **(10 points)** Simplify the following Boolean expression using Boolean algebra laws: $\overline{(A \cdot B)}$
    * Using De Morgan's theorem: $\overline{A} + \overline{B}$

3. **(10 points)** Using De Morgan's theorem simplify the following boolean expression: $\overline{A} + \overline{B}$
    * Using De Morgan's theorem: $\overline{A \cdot B}$
