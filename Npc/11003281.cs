using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003281: Asimov
/// </summary>
public class _11003281 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0404102807008247$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0404102807008248$
                // - I've been waiting for you. 
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
