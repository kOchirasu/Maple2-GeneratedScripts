using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003497: Temporary Dimensional Portal
/// </summary>
public class _11003497 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0727033607008730$
    // - A temporary portal for you, lost soul! Courtesy of $npcName:11003257$, genius mage!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0727033607008731$
                // - A temporary portal for you, lost soul! Now servicing the $map:52000134$ and the $map:52000149$.
                switch (selection) {
                    // $script:0727033607008732$
                    // - (Go to the $map:52000134$.)
                    case 0:
                        return 11;
                    // $script:0727033607008733$
                    // - (Stay here.)
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0727033607008734$
                // - You're on your way!
                return -1;
            case (12, 0):
                // $script:0727033607008735$
                // - Come find me if you change your mind.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
