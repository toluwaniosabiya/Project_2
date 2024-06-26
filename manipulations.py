import pandas as pd  # type: ignore

from datasets import Datasets

datasets = Datasets()


class BarChartBuilder:

    def __init__(
        self,
        dataset: pd.DataFrame = datasets.extract_data_for_national_effectiveness(),
    ) -> None:
        self.dataset = dataset

    def get_dropdown_options(self) -> list[dict]:
        dropdown_list = self.dataset.columns[-4:].tolist()
        dropdown_options = [{"label": f"{item}", "value": f"{item}"} for item in dropdown_list]

        return dropdown_options

    def supply_bar_chart_info(self, column: str) -> pd.Series:
        series = self.dataset[column].value_counts(normalize=True) * 100

        return series


class TableBuilder:

    def __init__(
        self,
        dataset: pd.DataFrame = datasets.extract_data_for_provision_types_and_places(),
    ) -> None:
        self.dataset = dataset

    def calculate_total_number_of_facilities(self, dataset: pd.DataFrame) -> int:
        df = dataset

        return len(df["Provision type"])

    def calculate_provision_types_breakdown(self, dataset: pd.DataFrame):
        df = dataset
        provision_type_breakdown = df["Provision type"].value_counts()

        return provision_type_breakdown

    def calculate_total_number_of_places(self, dataset: pd.DataFrame):
        df = dataset

        return int(df["Places"].sum())

    def calculate_places_by_provision_type(self, dataset: pd.DataFrame):
        df = dataset
        data = df.groupby("Provision type")["Places"].sum()

        return data


class LAFilter:
    def __init__(
        self,
        dataset: pd.DataFrame = datasets.extract_data_for_provision_types_and_places(),
    ) -> None:
        self.dataset = dataset

    def filter_dataset_by_LA(self, local_authority: str):
        filtered_dataset = self.dataset[self.dataset["Local authority"] == local_authority]

        return filtered_dataset

    def get_la_dropdown_options(self):
        dropdown_list = self.dataset["Local authority"].unique().tolist()
        dropdown_options = [{"label": f"{item}", "value": f"{item}"} for item in dropdown_list]

        return dropdown_options

    def get_la_effectiveness_dropdown_options(self):
        dropdown_list = self.dataset.columns[-5:].tolist()
        dropdown_options = [{"label": f"{item}", "value": f"{item}"} for item in dropdown_list]
        del dropdown_options[1:3]

        return dropdown_options

    def supply_la_level_bar_chart_info(self, data: pd.DataFrame, column: str):
        series = data[column].value_counts(normalize=True) * 100

        return series
