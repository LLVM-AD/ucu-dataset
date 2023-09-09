import csv
import argparse


def command_level_acc(true_dict, pred_dict) -> float:
    correct = 0
    total = 0
    for cid, true_labels in true_dict.items():
        if cid in pred_dict:
            pred_labels = pred_dict[cid]
            if len(true_labels) == len(pred_labels):
                correct += 1 if all([true_labels[i] == pred_labels[i] for i in range(len(true_labels))]) else 0
        total += 1
    acc = correct / total
    print(f"Command-level acc: {acc}")
    return acc


def question_level_acc(true_dict, pred_dict) -> float:
    correct = 0
    total = 0
    for cid, true_labels in true_dict.items():
        if cid in pred_dict:
            pred_labels = pred_dict[cid]
            if len(true_labels) == len(pred_labels):
                correct += sum([1 if true_labels[i] == pred_labels[i] else 0 for i in range(len(true_labels))])
        total += len(true_labels)
    acc = correct / total
    print(f"Question-level acc: {acc}")
    return acc


def open_true_csv(path="ucu.csv"):
    true_dict = dict()
    with open(path, 'r') as f:
        reader = csv.reader(f)
        fields = next(reader)
        for row in reader:
            command_id = int(row[0])
            labels = [1 if x == 'Yes' else 0 for x in row[2:]]
            true_dict[command_id] = labels
    return true_dict


def open_pred_csv(path):
    pred_dict = dict()
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            command_id = int(row[0])
            labels = [int(x) for x in row[1:]]
            pred_dict[command_id] = labels
    return pred_dict


parser = argparse.ArgumentParser()
parser.add_argument('--true_path', type=str, default='ucu.csv')
parser.add_argument('--pred_path', type=str, default='sample_pred.csv')

if __name__ == "__main__":
    args = parser.parse_args()
    tr_dict = open_true_csv(args.true_path)
    pr_dict = open_pred_csv(args.pred_path)
    command_level_acc(tr_dict, pr_dict)
    question_level_acc(tr_dict, pr_dict)
