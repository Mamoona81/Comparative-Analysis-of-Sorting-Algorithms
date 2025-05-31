import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load experimental data from CSV
data = pd.read_csv(r"E:\fj-MS\Algorithems-Dr Nergis\assignment\performance_analysis.csv")


# Generate Line Chart: Runtime vs Input Size for Each Algorithm
def plot_runtime_vs_input_size(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x="input_size", y="execution_time", hue="algorithm", marker="o")
    plt.title("Runtime vs Input Size for Sorting Algorithms")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.legend(title="Algorithm")
    plt.grid(True)
    plt.savefig("runtime_vs_input_size.png")
    plt.show()

# Generate Bar Chart: Performance Across Data Types
def plot_performance_across_data_types(data):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x="test_case", y="execution_time", hue="algorithm")
    plt.title("Performance Across Data Types")
    plt.xlabel("Test Case")
    plt.ylabel("Execution Time (seconds)")
    plt.legend(title="Algorithm")
    plt.grid(True)
    plt.savefig("performance_across_data_types.png")
    plt.show()

# Analyze Data and Provide Key Observations
def analyze_data(data):
    observations = []
    
    # Group by Algorithm
    algo_group = data.groupby("algorithm")
    for algo, group in algo_group:
        avg_runtime = group["execution_time"].mean()
        observations.append(f"{algo} has an average runtime of {avg_runtime:.4f} seconds across all test cases.")
    
    # Best Algorithm for Each Input Size
    size_group = data.groupby("input_size")
    for size, group in size_group:
        best_algo = group.loc[group["execution_time"].idxmin()]
        observations.append(f"For input size {size}, {best_algo['algorithm']} performed the best with a runtime of {best_algo['execution_time']:.4f} seconds.")
    
    # Best Algorithm for Each Test Case
    test_case_group = data.groupby("test_case")
    for test_case, group in test_case_group:
        best_algo = group.loc[group["execution_time"].idxmin()]
        observations.append(f"For test case {test_case}, {best_algo['algorithm']} performed the best with a runtime of {best_algo['execution_time']:.4f} seconds.")
    
    return observations

# Run Visualizations and Analysis
if __name__ == "__main__":
    plot_runtime_vs_input_size(data)
    plot_performance_across_data_types(data)
    obs = analyze_data(data)
    with open("analysis_observations.txt", "w") as f:
        f.write("\n".join(obs))
    print("Visualizations saved and analysis completed. Observations written to 'analysis_observations.txt'.")