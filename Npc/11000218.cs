using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000218: Billy
/// </summary>
public class _11000218 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000951$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000955$
                // - People should be good to each other. You reap what you sow, as they say...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
