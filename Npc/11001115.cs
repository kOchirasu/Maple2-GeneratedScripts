using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001115: Mamida
/// </summary>
public class _11001115 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003742$
    // - Would you be so kind as to help me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003745$
                // - Valle, where have you been? Ah... I don't think I know you. I'm sorry, I haven't been myself lately. I thought you were my daughter when I heard your footsteps. 
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
