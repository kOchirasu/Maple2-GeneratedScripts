using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001730: Informant B
/// </summary>
public class _11001730 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006975$
    // - I'm here!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0804172407007060$
                // - I've been waiting for you!
                switch (selection) {
                    // $script:0804172407007061$
                    // - Why are you here?
                    case 0:
                        return 40;
                    // $script:0804172407007062$
                    // - See anything interesting lately?
                    case 1:
                        return 41;
                }
                return -1;
            case (40, 0):
                // $script:0804172407007063$
                // - Heh heh... Most humans can't comprehend the importance of my work here. Don't look down on me just 'cause I'm small!
                return -1;
            case (41, 0):
                // $script:0804172407007064$
                // - But I can tell that you're more sensible then the other humans. You value meerkat ingenuity, yes? Not a thing happens here that we don't see.
                switch (selection) {
                    // $script:0804172407007065$
                    // - So, what have you seen lately?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0804172407007066$
                // - All kinds of people come through here, raising all sorts of ruckus. Sometimes they make angry noises at us because they can't get their security deposits back. Once time, I saw the guards drag away a human male because he wouldn't leave the pretty human female.
                switch (selection) {
                    // $script:0804172407007067$
                    // - $male:Which pretty human female?,female:You mean me?$
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:0804172407007068$
                // - $male:Lessee...,female:Nuh-uh!$ $npcName:11000515[gender:1]$. You know her? You better steer clear. She's pretty, but she's got thorns!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
