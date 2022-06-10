using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000074: Karl
/// </summary>
public class _11000074 : NpcScript {
    internal _11000074(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000345$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0831180407000346$ 
                // - Ever since I was appointed minister, the most important person in my life has become $npcName:11000075[gender:1]$. I live to protect her and assist her in all her affairs. 
                return true;
            case 20:
                // $script:0831180407000347$ 
                // - Your eyes tell me what kind of person you are, $MyPCName$, and so I believe I can trust you. Please continue to protect the peace of this world.
                return true;
            case 30:
                // $script:0831180407000348$ 
                // - The Land of Darkness is but a stop on the way to the Shadow World. The only way to lock that terrible place away again is to restore the Blue Lapenta.
                return true;
            case 40:
                // $script:1215110507009739$ 
                // - Do you need something?
                switch (selection) {
                    // $script:1215110407009728$
                    // - I've heard some unsettling rumors about $map:02000001$ lately.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1215110407009729$ 
                // - Bah, you don't listen to rumor and hearsay, do you?
                switch (selection) {
                    // $script:1215110407009730$
                    // - Well, I also have a photo...
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1215110407009731$ 
                // - Oh. Hm... Curious...
                switch (selection) {
                    // $script:1215110407009732$
                    // - What can you tell me about the photo?
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:1215110407009733$ 
                // - Hard to say, with the photograph being as blurry as it is. But I think I've seen a similar creature depicted in a tome from my family's library.
                switch (selection) {
                    // $script:1215110407009734$
                    // - Go on...
                    case 0:
                        Id = 44;
                        return false;
                }
                return true;
            case 44:
                // $script:1215110407009735$ 
                // - Long ago, the goddess of light did battle with a dark being, but she was unable to destroy him. The shapes in this picture are similar to its minions.
                // $script:1215110407009736$ 
                // - But that's impossible. That evil was banished from this world long ago.
                switch (selection) {
                    // $script:1215110407009737$
                    // - What else can you tell me about this "being?"
                    case 0:
                        Id = 45;
                        return false;
                }
                return true;
            case 45:
                // $script:1215110407009738$ 
                // - I've told you all I know. Hopefully I've answered your question. Now, if you don't mind, I have matters of state to attend to.
                return true;
            default:
                return true;
        }
    }
}
