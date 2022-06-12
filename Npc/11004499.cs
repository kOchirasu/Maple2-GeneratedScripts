using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004499: Mauritius
/// </summary>
public class _11004499 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012393$
    // - Hmm...? Have we met?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012394$
                // - Hmm...? Have we met?
                switch (selection) {
                    // $script:1227192907012395$
                    // - I came here on Sky Fortress.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012396$
                // - Oh, you're that famous hero! An honor to meet you.
                return 11;
            case (11, 1):
                // $script:1227192907012397$
                // - I'm part of the architectural research team. Take a look at this structure here! Incredible, isn't it? I've never seen such an elaborate design.
                return 11;
            case (11, 2):
                // $script:1227192907012398$
                // - Each brick and pillar fits perfectly. I've never seen something like this before.
                return 11;
            case (11, 3):
                // $script:1227192907012399$
                // - All of the buildings I've examined since we got here has been like this. I only wish I could see how they pulled this off!
                switch (selection) {
                    // $script:0114163707012719$
                    // - I'm a bit curious, too.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114163707012720$
                // - It's worth researching. This could revolutionize building techniques all over the empire.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.Next,
            (11, 3) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
