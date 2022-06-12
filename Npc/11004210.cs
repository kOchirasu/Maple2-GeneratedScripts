using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004210: Ruru
/// </summary>
public class _11004210 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806045807010666$
    // - Yaaaaaawn...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806045807010667$
                // - You want to try out some high-caliber mushsplosives? Just pick up a bomb and throw it.
                switch (selection) {
                    // $script:0806052007010672$
                    // - Right... And how do I pick stuff up again?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0806052107010672$
                // - You don't know? Just stand next to a bomb and the words "Pick Up" will pop up in the air as if by magic. Just press the corresponding button and you're ready to unleash the cleansing power of fire!
                switch (selection) {
                    // $script:0806052107010673$
                    // - ...None of that seems strange to you?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0806052107010674$
                // - No stranger than the voices in my head that tell me to burn things!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
