using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000220: Victor
/// </summary>
public class _11000220 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000962$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000964$
                // - Fellowstone Tower will be the greatest building in all of Maple World when it's finished. The blueprints alone took years to perfect. 
                return -1;
            case (30, 0):
                // $script:0831180407000965$
                // - When it's complete, people will flock from all over to see Fellowstone Tower. It'll be the crown jewel of Victoria Island!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
