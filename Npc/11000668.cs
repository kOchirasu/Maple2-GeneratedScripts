using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000668: Niro
/// </summary>
public class _11000668 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002711$
    // - WHAT?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002714$
                // - Wait, are you going to go down to the basement?
                switch (selection) {
                    // $script:0831180407002715$
                    // - Yep!
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002716$
                // - Ha! You're funny. I don't know how you got down here, but trust me when I say you NEVER want to go to the 2nd basement. There are some really scary guys down there.
                return 31;
            case (31, 1):
                // $script:0831180407002717$
                // - It's just as well, I don't feel like dealing with you myself. Go on, go to the basement. And don't say I didn't warn you. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
