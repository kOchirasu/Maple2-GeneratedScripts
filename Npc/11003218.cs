using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003218: Joddy
/// </summary>
public class _11003218 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008243$
    // - You gave me a big scare.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008244$
                // - How're you feeling?
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
