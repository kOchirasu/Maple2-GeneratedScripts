using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004333: Miel
/// </summary>
public class _11004333 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011573$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011574$
                // - Hello.
                return 10;
            case (10, 1):
                // $script:1010140307011575$
                // - My friend. It is pleasant to see your face.
                return 10;
            case (10, 2):
                // $script:1010140307011576$
                // - This place is beautiful, is it not?
                return 10;
            case (10, 3):
                // $script:1010140307011577$
                // - I have never before walked such a land, under such a sky... and yet it strikes me as familiar, all the same.
                return 10;
            case (10, 4):
                // $script:1010140307011578$
                // - Perhaps I am drawing nearer to the answers I seek.
                switch (selection) {
                    // $script:1010140307011579$
                    // - I'm sure you are!
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011580$
                // - Thank you. Your enthusiasm always lifts my spirits.
                switch (selection) {
                    // $script:1010140307011581$
                    // - Is $npcName:11001431[gender:0]$ with you?
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:1010140307011582$
                // - I asked him to accompany me, but I fear our vulpine friend declined my invitation. Oh, what I might have learned if he was here to aid me...
                return 30;
            case (30, 1):
                // $script:1010140307011583$
                // - A lack his cutting insight...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
