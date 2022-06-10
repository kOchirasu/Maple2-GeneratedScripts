using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001730: Informant B
/// </summary>
public class _11001730 : NpcScript {
    internal _11001730(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006975$ 
                // - I'm here!
                return true;
            case 30:
                // $script:0804172407007060$ 
                // - I've been waiting for you!
                switch (selection) {
                    // $script:0804172407007061$
                    // - Why are you here?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0804172407007062$
                    // - See anything interesting lately?
                    case 1:
                        Id = 41;
                        return false;
                }
                return true;
            case 40:
                // $script:0804172407007063$ 
                // - Heh heh... Most humans can't comprehend the importance of my work here. Don't look down on me just 'cause I'm small!
                return true;
            case 41:
                // $script:0804172407007064$ 
                // - But I can tell that you're more sensible then the other humans. You value meerkat ingenuity, yes? Not a thing happens here that we don't see.
                switch (selection) {
                    // $script:0804172407007065$
                    // - So, what have you seen lately?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0804172407007066$ 
                // - All kinds of people come through here, raising all sorts of ruckus. Sometimes they make angry noises at us because they can't get their security deposits back. Once time, I saw the guards drag away a human male because he wouldn't leave the pretty human female.
                switch (selection) {
                    // $script:0804172407007067$
                    // - $male:Which pretty human female?,female:You mean me?$
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:0804172407007068$ 
                // - $male:Lessee...,female:Nuh-uh!$ $npcName:11000515[gender:1]$. You know her? You better steer clear. She's pretty, but she's got thorns!
                return true;
            default:
                return true;
        }
    }
}
