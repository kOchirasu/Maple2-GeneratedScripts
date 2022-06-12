using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003054: Allon
/// </summary>
public class _11003054 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0102155907007617$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0102155907007620$
                // - Ah, $MyPCName$. I've been waiting for you. 
                return 30;
            case (30, 1):
                // $script:0102155907007621$
                // - This place is cold... desolate.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
