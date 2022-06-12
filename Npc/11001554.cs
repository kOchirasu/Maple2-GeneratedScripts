using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001554: Bory
/// </summary>
public class _11001554 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0415104107006020$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0421104907006043$
                // - I should've worn a wide-brimmed hat today. This sun is killing me.
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
