def to_camel_case(text):
    if len(text) == 0: return ""
    a = text.replace("_","-").split("-")
    return a[0] + ("".join(x.capitalize() for x in a[1:]))

print(to_camel_case(''), '', "An empty string was provided but not returned")
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior","to_camel_case('the_stealth_warrior') did not return correct value")
print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior","to_camel_case('The-Stealth-Warrior') did not return correct value")
print(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
print(to_camel_case("a-Pippi_is_cute"), )