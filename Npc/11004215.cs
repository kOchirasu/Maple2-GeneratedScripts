using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004215: Stellar Chest
/// </summary>
public class _11004215 : NpcScript {
    internal _11004215(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0808172007010849$ 
                // - <font color="#909090">(This $npcName:11004215$ can create gem dust to help you upgrade your gemstones.)</font>
                return true;
            case 10:
                // $script:0808172007010850$ 
                // - <font color="#909090">(Do you wish to create some $itemPlural:20301849$?)</font>
                switch (selection) {
                    // $script:0808172007010851$
                    // - (Create 1.)
                    case 0:
                        Id = 0; // TODO: 11 | 14
                        return false;
                    // $script:0808172007010852$
                    // - (Create 10.)
                    case 1:
                        Id = 0; // TODO: 21 | 24
                        return false;
                    // $script:0808172007010853$
                    // - (Not now.)
                    case 2:
                        Id = 15;
                        return false;
                }
                return true;
            case 11:
                // $script:0808172007010854$ 
                // - <font color="#909090">(Consume 10 $itemPlural:30001187$ and 1 $item:30001188$ to make 1 $item:20301849$?)</font> 
                switch (selection) {
                    // $script:0808172007010855$
                    // - (Create 1 $item:20301849$.)
                    case 0:
                        Id = 0; // TODO: 12 | 13
                        return false;
                }
                return true;
            case 12:
                // $script:0808172007010856$ functionID=1 
                // - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
                return true;
            case 13:
                // $script:0808172007010860$ 
                // - <font color="#909090">(Your bag is full. Return after making some space.)</font>
                return true;
            case 14:
                // $script:0808172007010861$ 
                // - <font color="#909090">(Insufficient materials. You need 10 $itemPlural:30001187$ and 1 $item:30001188$ to begin the conversion process.)</font>
                return true;
            case 15:
                // $script:0808172007010862$ 
                // - <font color="#909090">(The cube stands by.)</font>
                return true;
            case 21:
                // $script:0808172007010857$ 
                // - <font color="#909090">(Consume 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to make 10 $itemPlural:20301849$?)</font> 
                switch (selection) {
                    // $script:0808172007010858$
                    // - (Create 10 $itemPlural:20301849$.)
                    case 0:
                        Id = 0; // TODO: 22 | 13
                        return false;
                }
                return true;
            case 22:
                // $script:0808172007010859$ functionID=2 
                // - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
                return true;
            case 24:
                // $script:0809135407010882$ 
                // - <font color="#909090">(Insufficient materials. You need 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to begin the conversion process.)</font>
                return true;
            case 50:
                // $script:0911140307011157$ 
                // - <font color="#909090">(After you reach level 50, you can use $itemPlural:30001187$ and $itemPlural:30001188$ on this chest to make materials for upgrading gemstones.)</font>
                return true;
            default:
                return true;
        }
    }
}
