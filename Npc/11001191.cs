using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001191: Joanna
/// </summary>
public class _11001191 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016202007004164$
    // - I wish I could cast my worries into the wind... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016202007004167$
                // - I wish it would all just be over...  
                switch (selection) {
                    // $script:1016202007004168$
                    // - What's wrong?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1016202007004170$
                // - It's been one disaster after another, and I'm just too tired to fight anymore. Money is ruining my life. If I could live without it, I would've quit already.
                return 31;
            case (31, 1):
                // $script:1016202007004171$
                // - I got transferred to another department because of an argument with the head of the broadcasting station over my program. Journalism used to be about integrity! It was about telling the truth, not just covering what makes money! I just can't do it anymore. 
                return 31;
            case (31, 2):
                // $script:1022192907004266$
                // - I soldier on and cover what they tell me, acting like there's nothing wrong. But every day I die a little inside. Someone's got to stand up to them, I know that! But if I do, they'll just replace me with another yes-man...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
