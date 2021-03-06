using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004058: Orde
/// </summary>
public class _11004058 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010089$
    // - I'm... sorry about what happened to the leaders of Terrun Calibre.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010090$
                // - I'm... sorry about what happened to the leaders of Terrun Calibre.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
