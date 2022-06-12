using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000190: Mr. Hofmann
/// </summary>
public class _11000190 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000837$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000840$
                // - Do you know what's good about these black pine mushrooms?
                switch (selection) {
                    // $script:0831180407000841$
                    // - Nope.
                    case 0:
                        return 31;
                    // $script:0831180407000842$
                    // - I don't really care.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000843$
                // - Of course you don't. I'm sure you haven't seen them before, either. They're that rare. They're good for... Good for... 
                return 31;
            case (31, 1):
                // $script:0831180407000844$
                // - Ah... Mm... I can't remember all of a sudden. I've been so forgetful lately. I don't know what's wrong with me. 
                return -1;
            case (32, 0):
                // $script:0831180407000845$
                // - Is... that so? Well, I guess young folks like you usually don't take much interest in herbs, but... This is embarrassing. Ha ha ha.
                return -1;
            case (40, 0):
                // $script:0831180407000846$
                // - Do you have a house?
                switch (selection) {
                    // $script:0831180407000847$
                    // - Yes.
                    case 0:
                        return 41;
                    // $script:0831180407000848$
                    // - No.
                    case 1:
                        return 44;
                }
                return -1;
            case (41, 0):
                // $script:0831180407000849$
                // - Are you comfortable in your home?
                switch (selection) {
                    // $script:0831180407000850$
                    // - Yeah.
                    case 0:
                        return 42;
                    // $script:0831180407000851$
                    // - No.
                    case 1:
                        return 43;
                }
                return -1;
            case (42, 0):
                // $script:0831180407000852$
                // - I see. Good for you. I've got a house, too. And a wife and children. But I'm not comfortable in my own home.
                return 42;
            case (42, 1):
                // $script:0831180407000853$
                // - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
                return -1;
            case (43, 0):
                // $script:0831180407000854$
                // - I see. You're just like me then. I'm not comfortable in my own home either.
                return 43;
            case (43, 1):
                // $script:0831180407000855$
                // - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
                return -1;
            case (44, 0):
                // $script:0831180407000856$
                // - I see. I've got a house. And a wife and children. But I'm not comfortable in my own home.
                return 44;
            case (44, 1):
                // $script:0831180407000857$
                // - My sons never listen. They run wild all the time, screaming and fighting. And my wife nags at me all day long. At home, I can't rest for even a moment.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.Next,
            (43, 1) => NpcTalkButton.Close,
            (44, 0) => NpcTalkButton.Next,
            (44, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
