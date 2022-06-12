using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004266: Nine
/// </summary>
public class _11004266 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011207$
    // - Breathe in. Breathe out. Stare at the sea. Yes, yes, it's coming back to me now. You've taught me a valuable lesson again today, ocean.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011208$
                // - Breathe in. Breathe out. Stare at the sea. Yes, yes, it's coming back to me now. You've taught me a valuable lesson again today, ocean.
                return 10;
            case (10, 1):
                // $script:0911203207011209$
                // - Yes, ocean, you're right. I must start over with a heart of gratitude. I must devote myself to my training!
                switch (selection) {
                    // $script:0911203207011210$
                    // - Hiiiii! What are you doing?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011211$
                // - I am gazing upon the great ocean and filling my heart with peace. I thought the spirit of rock had died within me, but after discussing it with the sea, I realize it had just gone on a little break.
                switch (selection) {
                    // $script:0911203207011212$
                    // - What happened?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011213$
                // - My hands still tremble when I think back upon that day... It was the Maple rock festival, and thousands watched as I made a terrible mistake in the middle of my song. Since then, I've never been able to play that part right.
                switch (selection) {
                    // $script:0911203207011214$
                    // - And the ocean is helping you with that...
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0911203207011215$
                // - Yes! Thanks to the ocean's wise advice, I am once again filled with the spirit of rock. Can't you see it shining in my eyes?
                return 13;
            case (13, 1):
                // $script:0911203207011216$
                // - Come to my next concert, and you'll see for yourself that I've been transformed by the sea.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
