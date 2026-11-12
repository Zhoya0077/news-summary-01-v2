#!/usr/bin/env python3
"""Write a one-file English summary of 11 November 2026 world news.

No input files, no network. Writes UTF-8 text (1-2000 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, defaulting to /output/entry.txt.
"""
import os

SUMMARY = (
    "US-mediated talks in Abu Dhabi discussed a Russia-Ukraine prisoner exchange, officials said (Reuters). "
    "A tanker fire in the Strait of Hormuz heightened fears for energy shipping (Reuters; NYT). "
    "At COP31 in Antalya, negotiators wrangled over fossil-fuel phase-out language (AFP). "
    "US consumer prices rose 0.4% in October, keeping pressure on the Federal Reserve over rate cuts (AP). "
    "Ebola cases in Congo passed 11,000, health officials said, as responders raced to contain the outbreak (AP). "
    "President Tshisekedi's allies pushed a referendum law through Congo's parliament (Reuters). "
    "The US House voted 211-204 to shelve an impeachment effort against Defense Secretary Hegseth (AP). "
    "Nvidia said US authorities were investigating matters involving CEO Jensen Huang (AP). "
    "Japan weighed acquiring nuclear-powered submarines, a major shift in its defense posture (Asahi). "
    "Clashes in Ethiopia killed at least 65 people, local officials said (France 24). "
    "In the IPL, Hardik Pandya moved to Punjab and Arshdeep Singh to Mumbai in pre-auction trades (PTI). "
    "UK Prime Minister Andy Burnham ruled out rejoining the EU single market, saying a closer deal could add 0.4% to GDP (Azernews). "
    "Pope Leo XIV ended his Argentina visit at Lujan, telling one million young Argentines it is never too late to return to Christ (Gaudium Press). "
    "At the ASEAN summit in Manila, leaders sought a joint response to the Iran war's energy shock and Hormuz shutdown (Al Jazeera). "
    "Astronomers reported a likely supermassive neutron star, 1.8 to 2.8 solar masses, tugging a red giant in system J0008+0128 (Scientific American). "
    "Manchester United finalised a deal for Mauricio Pochettino as manager, with the club in the relegation zone (RealGM). "
    "Philippine GDP growth slowed to 2.1% in the third quarter, its fifth straight slowdown (Asianomist)."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(SUMMARY)


if __name__ == "__main__":
    main()
