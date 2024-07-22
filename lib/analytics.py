from os import path

import matplotlib.pyplot as plt
import pandas as pd


class Analytics:
    def __init__(self, data: list[dict[str:any]]) -> None:
        self.__df = pd.DataFrame(data).sort_values(by="date")

    def to_csv(self, title) -> pd.DataFrame:
        self.__df.to_csv(path.join("result", f"{title}.csv"))

    def chart(self, title: str, subtitle: str) -> None:
        x = self.__df["date"]
        y = self.__df["header_elapsed"]
        y2 = self.__df["size"] / 1000

        fig, ax1 = plt.subplots()
        ax1.plot(x, y, label="Elapsed")
        ax1.fill_between(x, y, color="#1f77b480")

        ax1.set_title(f"{title}\n{subtitle}")
        ax1.legend(loc="lower left")
        ax1.set_xlabel("Query")
        ax1.set_ylabel("Time (s)")
        fig.gca().set_xticks([])

        ax2 = ax1.twinx()

        ax2.set_ylabel("Size (kb)")
        ax2.plot(x, y2, label="Size", color="#f38518")
        ax2.legend(loc="lower right")
        ax2.set_ylim([0, y2.max() * 2])
        ax2.tick_params(axis="y")

        fig.tight_layout()
        fig.set_size_inches(8, 4)
        fig.savefig(path.join("result", f"{title} - {subtitle}.png"))
