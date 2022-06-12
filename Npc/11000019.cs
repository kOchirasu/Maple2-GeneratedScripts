using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000019: Terry
/// </summary>
public class _11000019 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000090$
    // - Hm hm hmmm, hm! Those marching songs always get stuck in my head.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000093$
                // - Hey there. First time in $map:02000062$?
                switch (selection) {
                    // $script:0831180407000094$
                    // - Yep!
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000095$
                // - Well, if you're trying to get to $map:02000001$, I've got some bad news for you.. We just had a big earthquake that split the road there in half. No one can make the journey now.
                return 31;
            case (31, 1):
                // $script:0831180407000096$
                // - As if that weren't bad enough, rough seas are preventing ships from entering or leaving the harbor. We're all stuck here!
                switch (selection) {
                    // $script:0831180407000097$
                    // - Is there no other way to get to $map:02000001$?
                    case 0:
                        return 32;
                    // $script:0831180407000098$
                    // - What about by air?
                    case 1:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0831180407000099$
                // - I've heard there's a wilderness path that connects $map:02000115$ and $map:02000116$, but no one's been taking it. Supposedly it's a bit... dangerous.
                switch (selection) {
                    // $script:1111011307007374$
                    // - Where's the path?
                    case 0:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:0831180407000100$
                // - Uhh... Lith isn't that kind of port, buddy.
                return -1;
            case (34, 0):
                // $script:1111011407007374$
                // - It's through a mountain path northwest of $map:02000062$. The path's been closed for ages, though. Too treacherous for most folks. I'd forget about it if I were you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
