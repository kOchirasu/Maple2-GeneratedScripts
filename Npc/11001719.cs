using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001719: Junta
/// </summary>
public class _11001719 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006970$
    // - You have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507007016$
                // - If things are to return to normal, then we must stay united. Don't forget that.
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
