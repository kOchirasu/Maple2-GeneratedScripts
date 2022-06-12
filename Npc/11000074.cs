using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000074: Karl
/// </summary>
public class _11000074 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30;40
    }

    // Select 0:
    // $script:0831180407000345$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000346$
                // - Ever since I was appointed minister, the most important person in my life has become $npcName:11000075[gender:1]$. I live to protect her and assist her in all her affairs. 
                return -1;
            case (20, 0):
                // $script:0831180407000347$
                // - Your eyes tell me what kind of person you are, $MyPCName$, and so I believe I can trust you. Please continue to protect the peace of this world.
                return -1;
            case (30, 0):
                // $script:0831180407000348$
                // - The Land of Darkness is but a stop on the way to the Shadow World. The only way to lock that terrible place away again is to restore the Blue Lapenta.
                return -1;
            case (40, 0):
                // $script:1215110507009739$
                // - Do you need something?
                switch (selection) {
                    // $script:1215110407009728$
                    // - I've heard some unsettling rumors about $map:02000001$ lately.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1215110407009729$
                // - Bah, you don't listen to rumor and hearsay, do you?
                switch (selection) {
                    // $script:1215110407009730$
                    // - Well, I also have a photo...
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1215110407009731$
                // - Oh. Hm... Curious...
                switch (selection) {
                    // $script:1215110407009732$
                    // - What can you tell me about the photo?
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:1215110407009733$
                // - Hard to say, with the photograph being as blurry as it is. But I think I've seen a similar creature depicted in a tome from my family's library.
                switch (selection) {
                    // $script:1215110407009734$
                    // - Go on...
                    case 0:
                        return 44;
                }
                return -1;
            case (44, 0):
                // $script:1215110407009735$
                // - Long ago, the goddess of light did battle with a dark being, but she was unable to destroy him. The shapes in this picture are similar to its minions.
                return 44;
            case (44, 1):
                // $script:1215110407009736$
                // - But that's impossible. That evil was banished from this world long ago.
                switch (selection) {
                    // $script:1215110407009737$
                    // - What else can you tell me about this "being?"
                    case 0:
                        return 45;
                }
                return -1;
            case (45, 0):
                // $script:1215110407009738$
                // - I've told you all I know. Hopefully I've answered your question. Now, if you don't mind, I have matters of state to attend to.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.SelectableDistractor,
            (44, 0) => NpcTalkButton.Next,
            (44, 1) => NpcTalkButton.SelectableDistractor,
            (45, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
