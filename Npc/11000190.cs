using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000190: Mr. Hofmann
/// </summary>
public class _11000190 : NpcScript {
    internal _11000190(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000837$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0831180407000840$ 
                // - Do you know what's good about these black pine mushrooms?
                switch (selection) {
                    // $script:0831180407000841$
                    // - Nope.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000842$
                    // - I don't really care.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000843$ 
                // - Of course you don't. I'm sure you haven't seen them before, either. They're that rare. They're good for... Good for... 
                // $script:0831180407000844$ 
                // - Ah... Mm... I can't remember all of a sudden. I've been so forgetful lately. I don't know what's wrong with me. 
                return true;
            case 32:
                // $script:0831180407000845$ 
                // - Is... that so? Well, I guess young folks like you usually don't take much interest in herbs, but... This is embarrassing. Ha ha ha.
                return true;
            case 40:
                // $script:0831180407000846$ 
                // - Do you have a house?
                switch (selection) {
                    // $script:0831180407000847$
                    // - Yes.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407000848$
                    // - No.
                    case 1:
                        Id = 44;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407000849$ 
                // - Are you comfortable in your home?
                switch (selection) {
                    // $script:0831180407000850$
                    // - Yeah.
                    case 0:
                        Id = 42;
                        return false;
                    // $script:0831180407000851$
                    // - No.
                    case 1:
                        Id = 43;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407000852$ 
                // - I see. Good for you. I've got a house, too. And a wife and children. But I'm not comfortable in my own home.
                // $script:0831180407000853$ 
                // - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
                return true;
            case 43:
                // $script:0831180407000854$ 
                // - I see. You're just like me then. I'm not comfortable in my own home either.
                // $script:0831180407000855$ 
                // - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
                return true;
            case 44:
                // $script:0831180407000856$ 
                // - I see. I've got a house. And a wife and children. But I'm not comfortable in my own home.
                // $script:0831180407000857$ 
                // - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
                return true;
            default:
                return true;
        }
    }
}
