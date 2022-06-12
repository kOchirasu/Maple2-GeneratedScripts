using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000406: Blake
/// </summary>
public class _11000406 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001642$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001644$
                // - Sometimes I'm afraid to look in the mirror.
                switch (selection) {
                    // $script:0831180407001645$
                    // - Why?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407001646$
                // - I might fall in love with myself!
                switch (selection) {
                    // $script:0831180407001647$
                    // - But I'm already in love with you!
                    case 0:
                        return 22;
                    // $script:0831180407001648$
                    // - I'm just gonna pretend I didn't hear that.
                    case 1:
                        return 23;
                }
                return -1;
            case (22, 0):
                // $script:0831180407001649$
                // - I know how difficult it is to resist my incredible charms. Don't hate me because I can't love you in return.
                return -1;
            case (23, 0):
                // $script:0831180407001650$
                // - Hey, hey! What are you looking at? Look at me! Hello! Hey, can't you hear me?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
