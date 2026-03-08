

def analyze_code(code):

    steps = []
    flow = []
    simulation = []
    execution_lines = []

    lines = code.split("\n")

    loop_var = None
    loop_limit = None

    loop_line = None
    condition_line = None
    print_line = None
    update_line = None

    even_odd_logic = False

    
    for idx, line in enumerate(lines):

        clean = line.strip()

        if not clean:
            continue

        
        if "=" in clean and "==" not in clean and not clean.startswith("while"):
            steps.append(f"Variable assignment: {clean}")

        
        if clean.startswith("while"):

            steps.append(f"Loop detected: {clean}")

            condition = clean.replace("while","").replace(":","").strip()

            if "<=" in condition:
                var, limit = condition.split("<=")
                loop_var = var.strip()
                loop_limit = int(limit.strip()) + 1

            elif "<" in condition:
                var, limit = condition.split("<")
                loop_var = var.strip()
                loop_limit = int(limit.strip())

            loop_line = idx

       
        if "% 2" in clean:
            even_odd_logic = True
            condition_line = idx
            steps.append("Conditional check detected")

        
        if "print" in clean:
            print_line = idx
            steps.append(f"Output statement: {clean}")

        
        if "+=" in clean:
            update_line = idx
            steps.append(f"Variable update: {clean}")

    
    if loop_var:

        flow = [
            "Start",
            "Initialize variable",
            "Check loop condition",
            "Evaluate conditional",
            "Print output",
            "Update variable",
            "Repeat"
        ]

    else:
        flow = ["Start", "Execute statements", "End"]

    
    if loop_var and loop_limit:

        for i in range(loop_limit):

            if loop_line is not None:
                execution_lines.append(loop_line)

            if print_line is not None:
                execution_lines.append(print_line)

            if update_line is not None:
                execution_lines.append(update_line)

            
            if "square" in code and "i * i" in code:

                square = i * i
                simulation.append(f"{loop_var} = {i} → print {square}")

            elif even_odd_logic:

                if i % 2 == 0:
                    simulation.append(f"{loop_var} = {i} → Even")
                else:
                    simulation.append(f"{loop_var} = {i} → Odd")

            else:
                simulation.append(f"{loop_var} = {i}")

    else:

        simulation.append("Program executes sequentially")

    return steps, flow, simulation, execution_lines