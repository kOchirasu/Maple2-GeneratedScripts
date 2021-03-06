using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004067: Chalk Graffiti
/// </summary>
public class _11004067 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010135$
    // - <font color="#909090">(You see a message that appears to be written in chalk.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010136$
                // - <font color="#909090">(You see a message that appears to be written in chalk.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010137$
                // - <font color="#909090">(The writing is barely legible.)</font>
                //   <i>Ah, my love, my love! Your blue eyes and wavy golden hair haunt me! There's no way you could know my feelings, but my heart will explode if I don't write them down!</i>
                return 10;
            case (10, 2):
                // $script:0619202207010138$
                // - <i>Are you an angel? I heard a tale that you were born from the goddess of light, but to me, you </i>are<i> the goddess of light!</i>
                return 10;
            case (10, 3):
                // $script:0619202207010139$
                // - <i>Can you blame me if I despise F? He is the only one who can be near you. Although I'm just one of many guards right now, one day I will be at your side!</i>
                return 10;
            case (10, 4):
                // $script:0625110307010359$
                // - <font color='#909090'>(This could be trouble for the empress...)</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
