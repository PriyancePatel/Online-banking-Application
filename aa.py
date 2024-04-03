import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def draw_earth():
    # Create a figure and axis with a Plate Carree projection
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Draw coastlines and borders
    ax.coastlines()
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', linewidth=0.5)

    # Set the extent to global
    ax.set_global()

    # Add a title
    ax.set_title('Earth')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    draw_earth()
