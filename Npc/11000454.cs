using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000454: Teo
/// </summary>
public class _11000454 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002006$
    // - I'm a seasoned sailor!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002009$
                // - Ahoy there! Have you ever seen a whale?
                switch (selection) {
                    // $script:0831180407002010$
                    // - Yes.
                    case 0:
                        return 31;
                    // $script:0831180407002011$
                    // - Nope.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002012$
                // - Bah, nonsense! I've been a fisherman my whole life, and only seen a whale once. And it was a teeny one at that! Me dream is to see the great blue whale just once before the sea takes me.
                return -1;
            case (32, 0):
                // $script:0831180407002013$
                // - Aye, they're an elusive catch. I've always wanted to see a blue whale myself.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
