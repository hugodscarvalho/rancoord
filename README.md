


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hugodscarvalho/rancoord">
    <img src="images/rancoord_logo.png" alt="RanCoord Logo" height="200">
  </a>
  <h3 align="center">RanCoord</h3>
  <p align="center">
    RanCoord is a Python package for random sampling of geographic coordinates!
    <br />
    <a href="https://github.com/hugodscarvalho/rancoord"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hugodscarvalho/rancoord">View Demo</a>
    ·
    <a href="https://github.com/hugodscarvalho/rancoord/issues">Report Bug</a>
    ·
    <a href="https://github.com/hugodscarvalho/rancoord/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<a href="https://github.com/hugodscarvalho/rancoord">
    <img src="images/rancoord_logo.png" alt="RanCoord Logo" height="80">
</a>

This project arises within the scope of research and development activities in the area of freight transport with respect to vehicle routing problems. Geographic coordinates are one of the most accurate means of identifying a location with extreme sensitivity.

Thus, with this project it is intended:
* Reduce the time and effort required to acquire geographic coordinates within a specific location
* Eliminate the need to use geographic data that do not fit a particular problem to be addressed
* Provide geographic coordinates in an extremely easy, fast and customized way to the user's needs

As time goes on, according to my availability and the feedback offered by users it is expected that new features will be included in this package that can make life easier for users addressing vehicle routing problems associated with geographic coordinates.
A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

The major frameworks used to build this project were:
* [Python](https://www.python.org/)
* [Folium](https://github.com/python-visualization/folium)
* [Project OSRM](http://project-osrm.org/)



<!-- GETTING STARTED -->
## Getting Started

This section presents how the package can be reached and installed.

### Where to get it

The source code is currently hosted on GitHub at: https://github.com/hugodscarvalho/rancoord

Binary installer for the latest released version are available at the Python Package Index (PyPI).

```sh
pip install rancoord
```

<!-- USAGE EXAMPLES -->
## Usage

In order to be able to generate a number of random geographic coordinates within a specific location it is necessary to create the polygon that encompasses it. The package provides three different ways to approach this prerequisite.

### 1. Use the default polygon
If you choose this option, there's no need to define it, the geographic randomizer module will already have it defined. Geographic data comprised in it:

```python
poly = Polygon(
    [
        (38.78562804689748, -9.47276949903965),
        (38.713870245772654, -9.139059782242775),
        (38.89740476139506, -9.055975675797463),
        (38.96871087768789, -8.969115019059181),
        (39.05061092686942, -8.92894625685215),
        (39.08579612091302, -9.407538175797463),
        (38.984457987516386, -9.397238493180275),
    ]
)
```
Map visualization:

<a href="https://github.com/hugodscarvalho/rancoord">
    <img src="images/default_location.png" alt="RanCoord Default Location">
</a>

### 2. Create your own polygon
If you choose this option, you will have to define the polygon using some geographic tool as the app from [Headwall Photonics](http://apps.headwallphotonics.com/), copy the coordinates, structure them and define de polygon.

<a href="https://github.com/hugodscarvalho/rancoord">
    <img src="images/headwall_photonics.PNG" alt="Headwall Photonics App">
</a>

### 3. Get a polygon using an address using 
If you choose this option, you can get a polygon based on the [bounding box](https://en.wikipedia.org/wiki/Minimum_bounding_box) of an address or location using *Noninatim*. 
```python
# Get the bounding box
bounding_box = nominatim_geocoder('Braga, Portugal')
# Create a polygon based on the previously created bounding box
poly = polygon_from_boundingbox(bounding_box)
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/hugodscarvalho/rancoord/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/hugodscarvalho/rancoord/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hugodscarvalho
[product-screenshot]: images/rancoord_logo.png
