import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import argparse


def plot_data(levels, totals, each_val, font_path, output_file):
    """
    Plot the data in a chart
    :param levels: The levels of membership on the board
    :param totals: The total number of members at each level
    :param each_val: The number of members in each group
    :param font_path: The path to the custom font
    :return:
    """
    # CSET color palette
    colors = ["#7AC4A5", "#B53A6D", "#003DA6", "F17F4C", "0B1F41"]

    r = range(len(levels))
    plt.figure(figsize=(14, 5))
    plt.rcParams.update({'font.size': 16})
    prop = font_manager.FontProperties(fname=font_path)
    plt.barh(r, each_val["Government"], color=colors[1], edgecolor="white", label="Government")
    plt.barh(r, each_val["Industry (State-Owned Enterprise)"], color=colors[0], hatch="x",
             left=np.array(each_val["Government"]), edgecolor="white", label="Industry (State-Owned Enterprise)")
    plt.barh(r, each_val["Industry (Not State-Owned Enterprise)"], color=colors[0],
             left=np.array(each_val["Government"]) + np.array(each_val["Industry (State-Owned Enterprise)"]),
             edgecolor="white", label="Industry (Not State-Owned Enterprise)")
    plt.barh(r, each_val["Academia"], color=colors[2],
             left=np.array(each_val["Industry (Not State-Owned Enterprise)"]) +
                  np.array(each_val["Industry (State-Owned Enterprise)"]) + np.array(each_val["Government"]),
             edgecolor="white",  label="Academia")

    for i, total in enumerate(totals):
        # Putting the total number after the bars
        plt.text(100 + 0.2, i, str(total), color='black', fontweight='bold')

    plt.legend(prop=prop, loc="lower center")
    plt.yticks(r, levels, fontproperties=prop)
    plt.xlabel("% of Members", fontproperties=prop)
    plt.savefig(output_file)
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", type=str, help="Name of output png file")
    parser.add_argument("font_path", type=str,
                        help="Path to the appropriate custom font font on your system")
    args = parser.parse_args()
    if "png" not in args.output_file:
        parser.print_help()
        exit()
    levels = ["Ordinary\n member", "Board \nmember", "Vice chair\n of board"]
    # We're hard-coding our data, which isn't great practice, but it's a very small amount of data
    # and a single visualization we want it for
    totals = [350, 189, 28]
    each_val = {"Industry (Not State-Owned Enterprise)": [309, 136, 13],
                "Industry (State-Owned Enterprise)": [27, 19, 10], "Government": [6, 17, 2], "Academia": [7, 17, 3]}
    for entry in each_val.keys():
        each_val[entry] = [(i/totals[index])*100 for index, i in enumerate(each_val[entry])]
    # Note: there is one "other" company we are not charting
    plot_data(levels, totals, each_val, args.font_path, args.output_file)


if __name__ == "__main__":
    main()