using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004478: Hani
/// </summary>
public class _11004478 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228141007012420$
    // - Blake is so... bedazzling! Don't you think so, too?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228141007012421$
                // - Blake is so... bedazzling! Don't you think so, too?
                switch (selection) {
                    // $script:1228141007012422$
                    // - Bedazzling. Sure. Let's say yes.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1228141007012423$
                // - It's like we're witnessing history. The day Blake set foot in the new world!
                return 11;
            case (11, 1):
                // $script:1228141007012424$
                // - Wanna join the new Blake Fan Club—Kritias Branch? I've got the paperwork right here!
                switch (selection) {
                    // $script:1228141007012425$
                    // - Oh no, something urgent just came up. Bye.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1228141007012426$
                // - Really? Shoot... Well, come back soon, before we fill up!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
