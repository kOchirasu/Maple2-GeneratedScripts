using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003204: Gogh
/// </summary>
public class _11003204 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0404083307008232$
    // - Please! Help! My people's princess is in danger!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008233$
                // - We'll be lost if we don't save the princess!
                return -1;
            case (20, 0):
                // $script:0404083307008234$
                // - Thank you for your help. I'll never forget this.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
