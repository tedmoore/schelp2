# Object Prototyping

**Categories:** Guides

*Writing runtime 'classes'*

**Related:** [IdentityDictionary](../Classes/IdentityDictionary.md)

You cannot create nor edit a class without recompiling the language... but what if you need that?
Object prototyping is a middle ground that lets you build class–like structures at runtime. It works by taking advantage of the class [IdentityDictionary](../Classes/IdentityDictionary.md) (often the subclass [Event](../Classes/Event.md) is used) and the special method [Object#-doesNotUnderstand](../Classes/Object.md#-doesnotunderstand). While there are some oddities with this approach, it is extremely powerful.

## Instance Variables (Members)
Instance variable–like things can be created by just adding keys to an [IdentityDictionary](../Classes/IdentityDictionary.md)


```
a = (meow: 10)
a.meow // 10
a.meow = 20;
a.meow // 20;
```


Unlike normal classes, you can create new instance variables at runtime.


```
a = (meow: 10)
a.woof = 4;
a.woof // 4
a.meow // 10
```




## Methods
By assigning a function to a key, you can call that function as if it were a normal instance method.

However, the [IdentityDictionary](../Classes/IdentityDictionary.md) is passed into the function as the first argument. Usually, we call this argument `self` as it performs a similar role to the keyword `this`.


```
a = ( speak: { |self, adverb| "I say '%' %.".format(self.word, adverb) } );
a.word = "meow";
a.speak(adverb: "loudly") // I say 'meow' loudly.
```


[Functions#Variable Arguments](../Reference/Functions.md#variable-arguments) also work.


```
a = ( speak: {|self... words, kwargs| "I say '%' %.".format(words, kwargs.asDict[\adverb]) } );

a.speak("meow", "woof", adverb: "loudly") // I say "[meow, woof]" loudly.
```




## Constructors
There is no direct way to mimic a constructor, but this isn't a problem, as we can simply make a function that returns the [IdentityDictionary](../Classes/IdentityDictionary.md).


```
(
var makeSpeaker = { |word|
    (
        word: word,
        speak: { |self, adverb| "I say \"%\" %.".format(self.word, adverb) }
    )
};

var cat = makeSpeaker.("meow");
var dog = makeSpeaker.("woof");

cat.speak("loudly").postln; // I say "meow" loudly.
dog.speak("quietly").postln; // I say "woof" quietly.
)
```




## Private Instance Variables (Members)
These can be implemented inside the constructor function as normal variables, however, you don't add them to the dictionary.


```
(
var makeSpeaker = {
    var secretWords = "I'm a cat";
    (
        assign_secret: { |self, secret| secretWords = secret },
        speak_secrets: { |self| "My secret is \"%\".".format(secretWords.value) }
    )
};

var p1 = makeSpeaker.();

p1.speak_secrets().postln; // My secret is "I'm a cat".
p1.assign_secret("I'm a dog");
p1.speak_secrets().postln; // My secret is "I'm a dog".
)
```




## Dangers
There are two drawbacks over classes.

The first, is that any key, including 'methods', can be overridden at any time. Essentially, what makes [IdentityDictionary](../Classes/IdentityDictionary.md) powerful, also makes it fragile and easy to break. The only way to avoid this mistake is by being vigilant when adding keys to an object prototype.

The second drawback is that you cannot have a key with the same name as a method in [Event](../Classes/Event.md) or any parent class, otherwise the real class's method will be called, not the pseudo–method you have written.


```
a = (numChannels: 10)
a.numChannels // 1
```


As seen above, one expects the value `10` to be returned, but instead [Object#-numChannels](../Classes/Object.md#-numchannels) is called and the value `1` returned.

There are two ways to mitigate this. **One**, use longer keys or names in snake case rather than pascal case: that is names_written_like_this, ratherThanNamesWrittenLikeThis, as SuperCollider only uses the latter.

**Two**, assign outside of the brackets, where a warning will be generated.


```
a = ();
a.numChannels = 30; // WARNING: ...
```




## Inheritance
This is implemented with [IdentityDictionary#-'parent' and 'proto' variables](../Classes/IdentityDictionary.md#-'parent'-and-'proto'-variables). Technically, this can be used to do more than inheritance, but only inheritance is shown here.

This is done by assigning the `parent` to another dictionary to lookup keys in.


```
a = (word: "meow" );
b = (speak: {|self| "I say \"%\".".format(self.word) } );
b.parent = a; // assign 'a' as a parent.
b.speak // I say "meow".
```


This is similar to how Javascript and other prototyping languages work.



