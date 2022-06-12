using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003828: Nairin
/// </summary>
public class _11003828 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0115140307009753$
    // - All systems are operational!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0115140307009754$
                // - How may I help you today, $male:Sir,female:Ma'am$?
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
