using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003164: Joddy
/// </summary>
public class _11003164 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0310134607008081$
    // - Whew! That was a close one.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0310134607008084$
                // - You really pulled me out of the fire.
                switch (selection) {
                    // $script:0310134607008085$
                    // - What are you talking about?
                    case 0:
                        return 31;
                    // $script:0310134607008086$
                    // - You're welcome, I guess?
                    case 1:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:0310134607008087$
                // - You drove off that big, bad doggy! If it weren't for you... Jeez, I'd really be in a pickle.
                switch (selection) {
                    // $script:0310134607008088$
                    // - You... do know how to fight, don't you?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0310134607008089$
                // - Sure do! I even fought a rogue $npcName:21000001$ once! I mean, I lost, but I sure gave it my best!
                return 32;
            case (32, 1):
                // $script:0310134607008090$
                // - Aw, jeez. I don't know about that look you're giving me...
                return -1;
            case (33, 0):
                // $script:0310134607008091$
                // - You really know a thing or two about being a hero, don't you? Wow!
                switch (selection) {
                    // $script:0310134607008092$
                    // - A hero...?
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0310134607008093$
                // - Yeah, a real, live hero! One day I'll be just like you. Just you wait!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
