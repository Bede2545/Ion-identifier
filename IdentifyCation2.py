
# Interactive Cation Identifier Using Bench Reagents

def identify_cation(reagent, observation):
    cation_properties = {
        "NaOH": {
            "white precipitate soluble in excess": "Al³⁺",
            "blue precipitate": "Cu²⁺",
            "green precipitate": "Fe²⁺",
            "brown precipitate": "Fe³⁺"
},
        "NH₃": {
            "white precipitate soluble in excess": "Zn²⁺",
            "deep blue solution": "Cu²⁺"
  },        
            
           "ammonia": {
              "white precipitate soluble in excess": "Zinc (II) ion",
              "deep blue solution": "copper (II) ion"  
},
        "HCl": {
            "white precipitate": "Ag⁺",
            "no reaction": "Na⁺ or K⁺"
},
        "Flame Test": {
            "crimson red": "Li⁺",
            "yellow": "Na⁺",
            "violet": "K⁺",
            "brick red": "Ca²⁺"
}
}

    reagent = reagent.strip()
    observation = observation.strip()

    result = cation_properties.get(reagent, {}).get(observation, "Unknown cation or observation not recognized.")
    return result


# 🌟 User input interface
print("🔬 Cation Identifier")
print("Enter reagent used (e.g., NaOH, NH₃,ammonia, HCl, Flame Test):")
reagent_input = input("> ").strip()

print("Describe the observation (e.g., blue precipitate, white precipitate soluble in excess):")
observation_input = input("> ").strip()

cation = identify_cation(reagent_input, observation_input)
print(f"🧪 Predicted cation: {cation}")
()