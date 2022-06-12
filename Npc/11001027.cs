using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001027: Palace Warden
/// </summary>
public class _11001027 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003503$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003506$
                // - Criminals are held here while waiting for sentencing. Once sentenced, they're sent to $map:02000124$.
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
