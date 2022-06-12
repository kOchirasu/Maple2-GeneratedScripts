using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003456: Muphaza
/// </summary>
public class _11003456 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008667$
    // - I am prepared to dedicate my life to the peace of $map:02000051$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008668$
                // - I am prepared to dedicate my life to the peace of $map:02000051$.
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
