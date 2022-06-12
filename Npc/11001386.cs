using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001386: Ahas
/// </summary>
public class _11001386 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217193307005386$
    // - Are you here to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228164407005730$
                // - If the development project is a success, it'll bring wealth and fame to $map:02010063$.
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
