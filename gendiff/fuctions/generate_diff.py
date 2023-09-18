import json


def generate_diff(file1, file2):
    with open(file1, 'r') as input_file1, open(file2, 'r') as input_file2:
        data1 = json.load(open(input_file1))
        data2 = json.load(open(input_file2))

        sorted_dict1 = dict(sorted(data1.items(), key=lambda x: x[0]))
        sorted_dict2 = dict(sorted(data2.items(), key=lambda x: x[0]))
        lines = ['{\n']
        for key in sorted_dict1:
            if key not in sorted_dict2:
                lines.append(f"- {key} : {data1[key]}\n")
            elif key in sorted_dict2 and sorted_dict1[key] != sorted_dict2[key]:
                lines.append(f"- {key} : {data1[key]}\n")
                lines.append(f"+ {key} : {data2[key]}\n")
            elif key in sorted_dict2 and sorted_dict1[key] == sorted_dict2[key]:
                lines.append(f"  {key} : {data1[key]}\n")
            else:
                lines.append('impossible\n')
        for key in sorted_dict2:
            if key not in sorted_dict1:
                lines.append(f"+ {key} : {data2[key]}\n")
        lines.append('}')
        return " ".join(lines)
