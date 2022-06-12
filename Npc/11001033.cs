using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001033: Vadell
/// </summary>
public class _11001033 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003533$
    // - Cough, cough... Please be careful. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003536$
                // - Ugh... I've been holed up in here so long. My head is killing me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
