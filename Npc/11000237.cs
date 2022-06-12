using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000237: Micky
/// </summary>
public class _11000237 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001013$
    // - Argh, this is awful! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001016$
                // - Hm? Why did you call me?
                switch (selection) {
                    // $script:0831180407001017$
                    // - What are you doing?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407001018$
                // - I don't know. Don't ask!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
