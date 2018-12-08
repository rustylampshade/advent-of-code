with open('inputs/8_1.txt', 'r') as aoc_input:
    vals = [int(v) for v in aoc_input.read().rstrip().split()]

def parse_tree(vals):
    node_count = vals.pop(0)
    metadata_count = vals.pop(0)
    metadata_total = 0
    node_value = 0

    child_node_values = []
    for _ in range(0, node_count):
        child_metadata_total, child_node_value = parse_tree(vals)
        metadata_total += child_metadata_total
        child_node_values.append(child_node_value)

    for _ in range(0, metadata_count):
        metadata_entry = vals.pop(0)
        metadata_total += metadata_entry
        if metadata_entry in range(1, node_count + 1):
            node_value += child_node_values[metadata_entry-1]

    if node_count == 0:
        node_value = metadata_total

    return metadata_total, node_value

print parse_tree(vals)