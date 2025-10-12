/*
Dependency: https://github.com/tedmoore/JSON-Writer-Supercollider
*/

(
~parse_args = {
	arg args;
	args.clump(2).collect{
		arg array;
		var d = IdentityDictionary.new;
		d[\name] = array[0];
		d[\default] = array[1];
		d;
	};
};

~parse_method = {
	arg m;
	var md = IdentityDictionary.new;
	md[\name] = m.name;
	md[\args] = ~parse_args.(m.keyValuePairsFromArgs);
	md;
};

~json = IdentityDictionary.new;
~json[\classes] = Class.allClasses.select{
	arg c;
	c.name.asString[..4] != "Meta_";
}.collect{
	arg c;
	var dict = IdentityDictionary.new;
	dict[\name] = c.name;
	dict[\subclasses] = c.subclasses.collect{arg sc; sc.name}.select{arg cs; cs.asString[..4] != "Meta_" } ? "none";
	dict[\superclasses] = c.superclasses.collect{arg sc; sc.name} ? "none";
	dict[\instancevariables] = c.instVarNames;
	dict[\classvariables] = c.classVarNames;
	dict[\methods] = c.methods.collect{arg m; ~parse_method.(m)};
	dict;
};
JSONWriter(~json,thisProcess.nowExecutingPath.dirname+/+"sc_classes.json");
)